# BetterUp Strategic Memo

## Ways this memo could be better

Since this is hypothetical, I can't present actual data or make recommendations based upon actual data or real systems. This, unfortunately, means much of this memo remains abstract. However, in a real memo, I want to include factual data about real-world events and make recommendations based on that data. For example, instead of stating a metric and target, I would want to state the current metric, why it matters to the business, and what steps we will take to improve the business results and, therefore, the metric.

I did include details about things I heard in my interviews with people; those facts are helpful, but I am keenly aware that my knowledge base about BetterUp is very limited. It is tough to make cogent recommendations about teams, sizes, organizations, or budgets because I don't know those details, and it doesn't make much sense to guess or make them up. So again, this stays very hypothetical. But I do expect that the recommendations here are directionally correct.

I wrote this over a long weekend; in practice when I write something like this, it happens over the course of weeks, and many people participate and provide input. So it lacks what diversity of thought brings, parallax.

I ran out of time and space to dig into team design, and philosophy. Given my lack of knowledge about the current teams and organization, this seems OK. Anything I write here beyond principles and generalities will be wrong. So I kept that section short.

## Introduction

The following memo outlines our current situation, presents a strategic diagnosis of the company, and recommends actions to be taken in the next 6, 12, and 24 months to address the diagnosis. While there are still many unknowns about the best ways to approach our current situation and deliver our mission, this memo strives to make concrete recommendations on steps to take now to address known acute issues. Much like climbing Mount Everest where we find ourselves as an organization is fairly well known, many people have walked this path before, many have succeeded, and many have not. Luckily you can hire experienced guides to help with your approach, the climb, and the summit.

In the following pages, I will make multiple recommendations about how to set up the organization. I will propose relevant and normative metrics and targets based on my experience with companies at this stage of growth and market fit. Noting that this document will be revised as the teams and I better understand our situation, challenges, customers, and members and then discern how best to create a sustainable and healthy product development organization.

As we tread forward into the future, we intend to listen to what our teams, the market, and customers tell us, then shift and change course as needed. We will act with as much grace, courage, passion, and integrity as we can muster. Nothing else will do.

## The Situation

BetterUp is on a mission to help people everywhere live their lives with greater clarity, purpose, and passion. We have spent several years building our brand, technology, and supply network in a vertically integrated strategy and have found success and traction in the market. Our pillars of success are a network of local, high-quality coaches, proprietary technology for building and managing our coaching network, and diverse expertise across internal operational supply teams from the onboarding through the service delivery process. We are now in the process of scaling up...fast, and it is challenging.

The product development team's charter is to scale up the technology organization to help the business grow in two dimensions: expanding the customer base by scaling internationally and reaching new customers through the innovation of new product offerings.

For the first five years of organizational growth, the health of the monolith technology platform has kept pace with the organization's evolution. But with the recent rapid influx of new team members focusing on new customer personas and problem domains, product velocity has decreased at a time when investments in innovation are more critical than ever.

In front of us, we face a massive mountain, and we are compelled to climb it. Like Everest, many have come before us; however, our situation is unique. We will encounter novel challenges and opportunities. It is not easy to simultaneously launch new products, expand markets, grow a healthy high functioning team, and maintain an effective, generative culture. This necessitates that we embrace our values deeply.

The path ahead will demand daring to make hard choices on limited information. It will take courage and grit to say "no" to the urgent to address the essential, and we will have to do this more often than is comfortable.

We will be challenged as we build new technology and operate at an ever greater scale in different markets; we will have to dig deep and hone our engineering excellence. We must remain empathetic and compassionate towards ourselves as we stumble and sometimes fail - and listen deeply to what our customers need and want. Building delightful iconic products that hum with joy and create experiences where people thrive requires creativity, playfulness, and perseverance to test, iterate, and experiment until we get it right.

Our diversity and unique perspectives will help us see what others can't or won't so that we can create entirely new experiences, products, and services that will help people everywhere live their lives with greater clarity, purpose, and passion. This is going to be so much fun!

## What now?

The crux of our strategic challenge is that our systems architecture and the teams which build, manage, and operate it are not designed or built to meet today's current and emerging needs.

For example, expansion into new markets (Gov, International) will require that we meet the requirements of multiple demanding laws and regulations which our platform currently does not accommodate. For example, to expand into Europe, we must comply with GDPR and to expand into the government sector, we must be FedRamp compliant.

As we explore new products and services, our monolith's tight coupling between services and data means discrete teams have many different dependencies to navigate and manage. Fortunately, these challenges are normative for an organization expanding its core business with new features, products, and market segments, so we have tried and true techniques for overcoming these challenges. We will explore those below.

To enable autonomous teams, it will be necessary to break up some of our existing monolith into discrete baskets of services. This decoupling will facilitate rapid change in different system capabilities like communications, coaching support, and customer onboarding. As we identify and isolate via API different system functions, we will retain the monolith and build outposts of functionality. This maneuver allows us to build autonomous teams around these new outposts of functionality while maintaining the core monolith. Over time the monolith may be completely deprecated in favor of services; however, we will only pull out functionality when we have clear data indicating the effort will net us a positive return in terms of business outcomes, team health, or performance.

To operate in new specialty environments, we plan to create functionality so that we can stamp-out "BetterUp in a Box" operating pods. The vision is that independent BetterUp instances will be configured and lightly customized to meet the needs of their operating environments. These pods may also support differentiated experiences per market and ideally allow for easy experimentation. An example key outcome of going with a "pod" architecture will be that we can keep our operations and data secure and separate by running pods in different AWS availability zones. This design will also enable easier layering of additional security or functionality to meet distinct customer requirements without complicating our other BetterUp instances.

To ensure we take advantage of our continuing growth and the scale efficiencies inherent in our business, we intend that a significant portion of our existing systems and technology will be crafted around supporting these pods. We intend that the core platform will enable each pod to minimize operating and go-to-market costs. Examples of functionality included in the core platform are customer onboarding, coach enablement, invoicing, billing, data warehousing, analytics, and other shared functions.

Concurrent with this, the product development organization must be prudently split up into discrete operating units to enable autonomy, velocity, and reliable software delivery based on the above maneuvers. Gaps in skills and staffing must also be addressed to ensure adequate capacity exists for each pod, core platform, and supporting function teams and departments.

Along the way the product development organization must also resolve the inherent tension, friction, and conflicts that result from the continuous creation of new products and services vs. the enduring need to improve and maintain our existing ones. This will require improving how we define, validate, prioritize, plan, and deliver software, systems, and, ultimately, delightful user experiences for our members, customers, and internal stakeholders. To do this well, we must choose the right metrics to manage, align the organization's incentives and structures so that it can deliver on many initiatives concurrently, and shift the product development culture to fit our current stage of growth and maturity.

## How will we know we are on track to address our challenges?

### Proposed 2023 Milestones

| End of Year Objective | '23 Q1 | '23 Q2 | '23 Q3 | '23 Q4 |
|---|---|---|---|---|
| BetterUp pods operational in GovCloud and EU AZs | Pod requirements & design complete | Beta pod in EU | Beta pod in govCloud | EU and GovCloud pods pilot |
| Core Platform built and operating smoothly | Core Platform requirements & initial design | Core Platform PH 1 | | |
| Domains identified, 2024 org design defined and appropriately staffed | Key domains identified, plan for staffing in progress | Supporting domains identified, hiring plan in motion | 80% of key hires in role, essential teams fully operational | Core and new business units fully staffed and operational |
| PD Org delivers 80% of Committed Epics as committed | PD Process designed and aligned across BU org | Pilot run w/ EOQ retrospective | Process and metric improvements in place | Delivery targets hit as committed |

This schedule is deliberately aggressive, it might seem hard, or even impossible. it is intended to challenge the team to answer the question: What would have to happen for us to actually do this?

## How will the organization be shaped to enable our new direction?

We know that we don't yet know with high precision exactly how the organization should be laid out, but we do know some tenets we want to follow in organizational design:

- Favor long-lived, autonomous teams who can solve problems end to end.
- Use tried and true methods for designing bounded contexts, DDD, or Wardley maps.
- Change incrementally, avoid whiplash, over-communicate, and get wide & early buy-in.
- Key initiatives and functions must have an empowered and highly experienced leader.
- Each team and department must have clear and understandable measures of success.
- Under-commit and over-deliver, institute WIP limits, focus on high situational awareness and continuous learning.
- Always keep the end in mind! We are working to solve business problems, not create idealized ivory tower organizations or systems. Pragmatism and efficiency are key!

## What are the next steps from here?

In December and January, we will convene several planning sessions to review and update this plan. Attendees will be from across the product organization, key stakeholders from our business, and select senior and above engineers who will be tasked to lead and drive key initiatives for 2023.

The outputs of those discussions will be several guiding documents, a high-level plan, a future target architecture, and process documents updating our engineering SDLC, and our product development process. We may also revisit leveling guides, and engineering expectation documents, and ensure we have clarity on how engineering and product interoperate.

---

## FAQ

**Q: What are the key metrics to measure success for the product development organization?**
A: We intend to hold teams accountable for delivering 80% of the epics that they commit to for a given quarter.

**Q: Do you think the above schedule is achievable? Are you crazy or something?**
A: Laugh, nope, not crazy. However, aggressive timelines focus the mind and create urgency for delivery. We have made large investments in people and technology, those investments must pay off quickly. Furthermore, our mission is very important and must be taken wide!

**Q: Are you sure this will work?**
A: The plan presented has worked in several different scaling organizations, so it is likely to work well here. However – we plan to replan. We will be reviewing this strategy and policy recommendations regularly to make sure we are confident we will deliver our mission as quickly as possible.

**Q: Why did you choose epics delivered per commitment per quarter vs. say using OKRs, isn't that gameable by teams?**
A: Engineering teams, when they grow through organizational scaling breakpoints (100, 300, 1000 FTEs) often need to get their groove back in terms of delivery. Setting an easy-to-understand target of 80% of committed epics delivered, with comprehensive specifics on what an epic is, why it matters, and who is accountable for its results, creates powerful incentives for fixing issues in prioritization, planning, and execution. All of those functions require revolution at org scaling breakpoints.
