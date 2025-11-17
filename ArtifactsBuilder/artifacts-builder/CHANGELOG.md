# Changelog

All notable changes to the Artifacts Builder skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-16

### Added - Initial AISkills Integration

This is the initial integration of the Artifacts Builder skill from Anthropic's official skills repository into the AISkills collection.

#### Core Functionality
- **React 18 + TypeScript** project initialization via `init-artifact.sh`
- **Single-file bundling** via `bundle-artifact.sh` using Parcel and html-inline
- **40+ shadcn/ui components** pre-installed and ready to use
- **Tailwind CSS 3.4.1** with complete theming system
- **Radix UI primitives** for accessible component foundations
- **Path aliases** (`@/components`, `@/lib`, `@/hooks`) configured out of the box
- **Node 18+ compatibility** with automatic Vite version detection

#### Component Library (40+ Components)

**Layout & Structure**
- Card (with Header, Content, Footer)
- Separator
- Aspect Ratio
- Resizable panels
- Scroll Area

**Navigation**
- Navigation Menu
- Breadcrumb
- Menubar
- Tabs

**Forms & Inputs**
- Form (React Hook Form + Zod integration)
- Input, Textarea
- Select, Checkbox, Radio Group
- Switch, Slider
- Calendar (react-day-picker)
- Command (⌘K palette)

**Feedback & Status**
- Alert
- Toast, Sonner (toast notifications)
- Progress
- Skeleton
- Badge

**Overlays & Dialogs**
- Dialog, Sheet, Drawer
- Popover, Tooltip, Hover Card
- Context Menu, Dropdown Menu

**Data Display**
- Table
- Accordion, Collapsible
- Carousel (Embla Carousel)
- Avatar

**Interactive Elements**
- Button
- Toggle, Toggle Group

**Utilities**
- Label
- cn() utility (clsx + tailwind-merge)
- useToast hook

#### Documentation Enhancements
- **Comprehensive README.md** (1,800+ words)
  - Complete tech stack overview
  - Quick start guide
  - Full component library reference
  - 5 real-world artifact examples
  - Best practices for architecture, performance, accessibility
  - Advanced topics (custom components, theming, state persistence)
  - Troubleshooting guide
  - Resource links

- **Integration with AISkills Ecosystem**
  - Peer review workflows with Gemini and Codex skills
  - Iterative development patterns
  - Quality assurance integration

- **Design Philosophy**
  - Anti-"AI slop" guidelines
  - Avoiding generic aesthetic patterns
  - Intentional design choices

#### Example Artifact Patterns
1. **Interactive Dashboard** - Data visualization with filtering and search
2. **Multi-Step Form** - Complex forms with validation and progress tracking
3. **Task Management App** - Kanban-style boards with drag-and-drop
4. **Data Explorer** - Interactive data browsing and export
5. **Interactive Game** - State management and user interaction

#### Dependencies Included

**Core**
- React 18.x
- TypeScript 5.x
- Vite 5.4.11+ (Node-version aware)

**Styling**
- Tailwind CSS 3.4.1
- tailwindcss-animate
- class-variance-authority
- clsx, tailwind-merge

**UI Components**
- @radix-ui/react-accordion
- @radix-ui/react-aspect-ratio
- @radix-ui/react-avatar
- @radix-ui/react-checkbox
- @radix-ui/react-collapsible
- @radix-ui/react-context-menu
- @radix-ui/react-dialog
- @radix-ui/react-dropdown-menu
- @radix-ui/react-hover-card
- @radix-ui/react-label
- @radix-ui/react-menubar
- @radix-ui/react-navigation-menu
- @radix-ui/react-popover
- @radix-ui/react-progress
- @radix-ui/react-radio-group
- @radix-ui/react-scroll-area
- @radix-ui/react-select
- @radix-ui/react-separator
- @radix-ui/react-slider
- @radix-ui/react-slot
- @radix-ui/react-switch
- @radix-ui/react-tabs
- @radix-ui/react-toast
- @radix-ui/react-toggle
- @radix-ui/react-toggle-group
- @radix-ui/react-tooltip

**Additional Libraries**
- sonner (toast notifications)
- cmdk (command palette)
- vaul (drawer component)
- embla-carousel-react
- react-day-picker
- react-resizable-panels
- date-fns
- react-hook-form
- @hookform/resolvers
- zod (validation)

**Build Tools**
- Parcel (bundling)
- @parcel/config-default
- parcel-resolver-tspaths
- html-inline
- pnpm (package manager)

#### Scripts

**init-artifact.sh**
- Creates new React + TypeScript project
- Configures Tailwind CSS with shadcn/ui theme
- Installs all dependencies
- Extracts 40+ pre-built components
- Sets up path aliases
- Generates components.json config
- Node version detection (18+ required)
- Vite version pinning for compatibility

**bundle-artifact.sh**
- Builds React app with Parcel
- Inlines all assets (JS, CSS, fonts, images)
- Creates single self-contained HTML file
- No source maps (optimized for sharing)
- File size reporting

#### Technical Features
- **TypeScript strict mode** enabled
- **Path alias resolution** in both TypeScript and Vite
- **Parcel tspaths resolver** for build-time alias support
- **Dark mode support** via next-themes
- **CSS custom properties** for theming
- **Accessibility** built-in via Radix UI primitives
- **Zero runtime dependencies** in bundled artifact (all inlined)

### Source

Original skill from [anthropics/skills](https://github.com/anthropics/skills/tree/main/artifacts-builder)

**License**: Apache License 2.0
**Copyright**: Anthropic PBC

### Integration Notes

This skill has been integrated into the AISkills collection with:
- Enhanced documentation for standalone use
- Peer review workflow integration (Gemini, Codex)
- Best practices aligned with AISkills quality standards
- Comprehensive component reference
- Real-world example patterns
- Troubleshooting and advanced usage guides

### Known Limitations

1. **Artifact Size**: While bundled artifacts are self-contained, very large applications may hit Claude.ai's artifact size limits. Keep bundles under 500KB when possible.

2. **External API Calls**: Artifacts run in the browser with CORS restrictions. External API calls may require proxy services or public CORS-enabled endpoints.

3. **State Persistence**: Artifacts reset on page reload unless using localStorage or other browser storage APIs.

4. **No Server-Side Logic**: Artifacts are frontend-only. Backend functionality requires external services.

5. **Browser Compatibility**: Bundled artifacts target modern browsers (Chrome, Firefox, Safari, Edge). IE11 is not supported.

### Future Enhancements

Potential improvements for future versions:

- **Component gallery** - Interactive showcase of all components
- **Template artifacts** - Pre-built starting points for common use cases
- **Animation library** - Framer Motion or similar for advanced animations
- **Chart components** - Recharts or similar for data visualization
- **Real-time data** - WebSocket examples for live updates
- **Progressive Web App** - Service worker and offline support patterns
- **Testing utilities** - Vitest setup for component testing

### Migration Guide

Not applicable for v1.0.0 (initial release).

### Credits

**Original Skill**: Anthropic PBC
**Integration & Documentation**: AISkills Collection
**Component Library**: shadcn/ui by shadcn
**UI Primitives**: Radix UI
**Styling**: Tailwind Labs

---

For the latest updates and source code, visit:
- **AISkills Repository**: https://github.com/leegonzales/AISkills
- **Anthropic Skills**: https://github.com/anthropics/skills
- **shadcn/ui**: https://ui.shadcn.com

## Version Format

Versions follow semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Breaking changes to skill interface or workflow
- **MINOR**: New features, components, or significant enhancements
- **PATCH**: Bug fixes, documentation updates, minor improvements
