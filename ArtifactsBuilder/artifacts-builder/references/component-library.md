# shadcn/ui Component Library Reference

Pre-installed components available after `init-artifact.sh`. Import from `@/components/ui/<name>`.

## Layout & Navigation

| Component | Import | Use For |
|-----------|--------|---------|
| `Card` | `card` | Content containers with header/footer |
| `Dialog` | `dialog` | Modal overlays |
| `Sheet` | `sheet` | Slide-out side panels |
| `Tabs` | `tabs` | Tabbed content switching |
| `NavigationMenu` | `navigation-menu` | Top-level site navigation |
| `Sidebar` | `sidebar` | App sidebar with collapsible sections |
| `Accordion` | `accordion` | Collapsible content sections |
| `Collapsible` | `collapsible` | Toggle visibility of content |
| `ScrollArea` | `scroll-area` | Custom scrollable regions |
| `Separator` | `separator` | Visual dividers |
| `ResizablePanel` | `resizable` | Drag-to-resize panel layouts |

## Form & Input

| Component | Import | Use For |
|-----------|--------|---------|
| `Button` | `button` | Actions and submissions |
| `Input` | `input` | Text fields |
| `Textarea` | `textarea` | Multi-line text |
| `Select` | `select` | Dropdown selection |
| `Checkbox` | `checkbox` | Boolean toggles |
| `RadioGroup` | `radio-group` | Single selection from options |
| `Switch` | `switch` | On/off toggles |
| `Slider` | `slider` | Range value selection |
| `DatePicker` | `date-picker` | Date selection (uses Calendar) |
| `Form` | `form` | react-hook-form integration |

## Data Display

| Component | Import | Use For |
|-----------|--------|---------|
| `Table` | `table` | Structured data rows |
| `DataTable` | `data-table` | Sortable/filterable tables (TanStack) |
| `Badge` | `badge` | Status labels, tags |
| `Avatar` | `avatar` | User profile images |
| `Progress` | `progress` | Completion bars |
| `Chart` | `chart` | Data visualization (Recharts wrapper) |

## Feedback & Overlay

| Component | Import | Use For |
|-----------|--------|---------|
| `Alert` | `alert` | Inline status messages |
| `AlertDialog` | `alert-dialog` | Confirmation prompts |
| `Toast` / `Sonner` | `sonner` | Ephemeral notifications |
| `Tooltip` | `tooltip` | Hover context |
| `Popover` | `popover` | Click-triggered floating content |
| `HoverCard` | `hover-card` | Rich hover previews |
| `Skeleton` | `skeleton` | Loading placeholders |

## Anti-Slop Reminders

- Avoid centering everything -- use asymmetric layouts
- Skip purple/blue gradients -- use flat colors or subtle texture
- Vary border-radius -- not everything needs `rounded-lg`
- Mix component sizes -- uniform sizing looks generated
- Use `prose` class for long-form text instead of custom typography
