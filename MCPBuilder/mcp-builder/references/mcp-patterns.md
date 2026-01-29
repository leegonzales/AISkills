# Common MCP Server Patterns

Reusable patterns for building effective MCP servers. Supplement to the main guide.

## Pattern 1: Paginated List with Smart Defaults

```python
@mcp.tool()
async def list_items(
    query: str = "",
    limit: int = 25,
    offset: int = 0,
    format: Literal["concise", "detailed"] = "concise",
) -> str:
    """List items with optional search. Returns concise summaries by default.
    Use format='detailed' only when agent needs full metadata."""
    results = await api.search(query, limit=limit, offset=offset)
    if format == "concise":
        return "\n".join(f"- {r.name} (id:{r.id})" for r in results)
    return json.dumps([r.to_dict() for r in results], indent=2)
```

**Why:** Agents burn context on verbose output. Default to concise; let them opt into detail.

## Pattern 2: Composite Workflow Tool

```python
@mcp.tool()
async def schedule_meeting(
    title: str, attendees: list[str], duration_minutes: int = 30
) -> str:
    """Check all attendees' availability and create meeting in one call.
    Returns created event details or conflict information."""
    conflicts = await check_availability(attendees)
    if conflicts:
        return f"Conflicts found: {format_conflicts(conflicts)}"
    event = await create_event(title, attendees, duration_minutes)
    return f"Meeting '{title}' created: {event.url}"
```

**Why:** Combining check + create into one tool saves the agent a round-trip.

## Pattern 3: Actionable Error Messages

```python
except RateLimitError:
    return (
        "Rate limited. Wait 60 seconds before retrying. "
        "Consider using limit=10 to reduce request size."
    )
except NotFoundError as e:
    return (
        f"Resource '{resource_id}' not found. "
        f"Use list_resources to find valid IDs. "
        f"Common mistake: using name instead of ID."
    )
```

**Why:** Agents need to know what to do next, not just what went wrong.

## Pattern 4: Truncation with Signal

```python
CHARACTER_LIMIT = 25_000

def truncate_response(text: str) -> str:
    if len(text) <= CHARACTER_LIMIT:
        return text
    truncated = text[:CHARACTER_LIMIT]
    return (
        f"{truncated}\n\n"
        f"[TRUNCATED: {len(text)} chars total. "
        f"Use offset/limit parameters to paginate.]"
    )
```

**Why:** Silent truncation loses information. Tell the agent data was cut and how to get the rest.

## Pattern 5: Read-Only vs Mutating Annotations

```python
@mcp.tool(annotations={
    "readOnlyHint": True,
    "openWorldHint": True,
})
async def search_docs(query: str) -> str: ...

@mcp.tool(annotations={
    "readOnlyHint": False,
    "destructiveHint": True,
    "idempotentHint": False,
})
async def delete_item(item_id: str) -> str: ...
```

**Why:** Annotations help clients enforce safety policies (e.g., requiring confirmation for destructive tools).

## Checklist Before Shipping

- [ ] Every tool has concise/detailed format option
- [ ] All errors suggest a next action
- [ ] Responses stay under 25K characters
- [ ] Read-only tools annotated as such
- [ ] Tool descriptions include "when to use" and "when NOT to use"
