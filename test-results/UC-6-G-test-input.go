// Package evolution provides the core evolution engine for prompt evolution
package evolution

import (
	"crypto/rand"
	"errors"
	"fmt"
	"log"
	"math/big"
	"sync"
	"time"

	"github.com/leegonzales/prompt-evolve/pkg/api"
)

// Engine represents the core evolution engine that drives the prompt evolution process
type Engine struct {
	config         api.EvolutionConfig
	population     api.PopulationManager
	fitnessEval    api.FitnessEvaluator
	currentGen     int
	bestIndividual *api.Individual
}

// NewEngine creates a new evolution engine with the given configuration
func NewEngine(config api.EvolutionConfig, pop api.PopulationManager, evaluator api.FitnessEvaluator) (*Engine, error) {
	// Validate configuration
	if err := validateConfig(config); err != nil {
		return nil, fmt.Errorf("invalid configuration: %w", err)
	}

	if pop == nil {
		return nil, errors.New("population manager cannot be nil")
	}

	if evaluator == nil {
		return nil, errors.New("fitness evaluator cannot be nil")
	}

	return &Engine{
		config:      config,
		population:  pop,
		fitnessEval: evaluator,
		currentGen:  0,
	}, nil
}

// Evolve runs the evolution process for the configured number of generations
func (e *Engine) Evolve() (*api.EvolutionResult, error) {
	if e.config.Generations <= 0 {
		return nil, errors.New("number of generations must be greater than 0")
	}

	// Initialize population
	err := e.population.Initialize()
	if err != nil {
		return nil, fmt.Errorf("failed to initialize population: %w", err)
	}

	// Main evolution loop
	startTime := time.Now()
	for e.currentGen < e.config.Generations {
		// Evaluate fitness of all individuals
		err := e.evaluatePopulation()
		if err != nil {
			return nil, fmt.Errorf("fitness evaluation failed at generation %d: %w", e.currentGen, err)
		}

		// Track the best individual from this generation
		best := e.population.GetBestIndividual()
		if e.bestIndividual == nil || best.Fitness > e.bestIndividual.Fitness {
			e.bestIndividual = best
			log.Printf("New best at generation %d: %.4f", e.currentGen, best.Fitness)
		}

		// Break if we've reached the final generation
		if e.currentGen == e.config.Generations-1 {
			break
		}

		// Breed next generation
		err = e.breedNextGeneration()
		if err != nil {
			return nil, fmt.Errorf("breeding failed at generation %d: %w", e.currentGen, err)
		}

		e.currentGen++
		log.Printf("Generation %d/%d complete", e.currentGen, e.config.Generations)
	}

	// Prepare results
	duration := time.Since(startTime)
	if e.bestIndividual == nil {
		return nil, errors.New("evolution completed but no best individual was found")
	}

	return &api.EvolutionResult{
		BestPrompt:        e.bestIndividual.Prompt,
		FitnessScore:      e.bestIndividual.Fitness,
		Generations:       e.currentGen + 1,
		TotalTime:         duration,
		EvaluationCount:   e.population.GetEvaluationCount(),
		InitialPrompt:     e.config.InitialPrompt,
		EvolutionProgress: e.population.GetEvolutionProgress(),
	}, nil
}

// breedNextGeneration creates the next generation of prompts
func (e *Engine) breedNextGeneration() error {
	// Selection - choose parents based on fitness
	parents, err := e.population.SelectParents(e.config.SelectionPressure)
	if err != nil {
		return fmt.Errorf("parent selection failed: %w", err)
	}

	// Validate we have parents
	if len(parents) == 0 {
		return errors.New("no parents selected for breeding")
	}

	// Create new generation through crossover and mutation
	offspring := make([]*api.Individual, 0, e.config.PopulationSize)

	for len(offspring) < e.config.PopulationSize {
		// Select two parents (with bounds checking)
		parent1 := parents[len(offspring) % len(parents)]
		parent2 := parents[(len(offspring) + 1) % len(parents)]

		var child *api.Individual

		// Apply crossover with probability
		if randf() < e.config.CrossoverRate && parent1.Prompt != parent2.Prompt {
			childPrompt := e.crossover(parent1.Prompt, parent2.Prompt)
			child = &api.Individual{Prompt: childPrompt}
		} else {
			// No crossover, clone parent1
			child = &api.Individual{Prompt: parent1.Prompt}
		}

		// Apply mutation with probability
		if randf() < e.config.MutationRate {
			child.Prompt = e.mutate(child.Prompt)
		}

		offspring = append(offspring, child)
	}

	// Replace old generation with new generation
	return e.population.ReplacePopulation(offspring)
}

// crossover combines two parent prompts to produce a child prompt
func (e *Engine) crossover(parent1, parent2 string) string {
	// Simple implementation - can be expanded with more sophisticated crossover methods
	if len(parent1) == 0 || len(parent2) == 0 {
		if len(parent1) > 0 {
			return parent1
		}
		return parent2
	}

	// Point crossover - split at random point
	splitPoint := randInt(1, min(len(parent1), len(parent2))-1)
	return parent1[:splitPoint] + parent2[splitPoint:]
}

// mutate applies random mutations to a prompt
func (e *Engine) mutate(prompt string) string {
	// Simple implementation - can be expanded with more sophisticated mutation methods
	// This is a placeholder - real implementation would have more intelligent mutations
	if len(prompt) == 0 {
		return prompt
	}

	// Convert to runes to handle UTF-8 properly
	runes := []rune(prompt)

	// Choose a random position
	pos := randInt(0, len(runes)-1)

	// Simple character substitution
	// In a real implementation, we would have multiple mutation strategies
	substitutions := []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.")
	runes[pos] = substitutions[randInt(0, len(substitutions)-1)]

	return string(runes)
}
