# Playwright Selector Strategies

## Selector Priority (Best to Worst)

| Priority | Selector Type | Example | Why |
|----------|--------------|---------|-----|
| 1 | Role | `getByRole('button', { name: 'Submit' })` | Accessible, resilient to markup changes |
| 2 | Label/Text | `getByLabel('Email')`, `getByText('Sign in')` | User-visible, stable |
| 3 | Placeholder | `getByPlaceholder('Search...')` | Visible to users |
| 4 | Test ID | `getByTestId('submit-btn')` | Explicitly stable, decoupled from UI |
| 5 | CSS | `page.locator('.btn-primary')` | Fragile, but sometimes necessary |
| 6 | XPath | `page.locator('//div[@class="x"]')` | Last resort only |

## Locator API (Preferred over Raw Selectors)

```javascript
// GOOD: Locator-based (auto-waits, auto-retries)
await page.getByRole('button', { name: 'Save' }).click();
await page.getByLabel('Username').fill('testuser');
await page.getByText('Welcome back').isVisible();

// AVOID: Raw selectors (no auto-wait semantics)
await page.click('button.save');  // deprecated pattern
```

## Filtering and Chaining

```javascript
// Filter by text within a role
page.getByRole('listitem').filter({ hasText: 'Product A' });

// Chain locators (scope narrowing)
page.locator('.sidebar').getByRole('link', { name: 'Settings' });

// Nth element
page.getByRole('listitem').nth(2);

// Filter by child locator
page.getByRole('listitem').filter({
  has: page.getByRole('button', { name: 'Delete' })
});
```

## Waiting Strategies

```javascript
// GOOD: Wait for specific condition
await page.waitForSelector('.results-loaded');
await page.getByRole('heading', { name: 'Dashboard' }).waitFor();
await page.waitForURL('**/dashboard');
await page.waitForLoadState('networkidle');

// BAD: Fixed timeouts
await page.waitForTimeout(3000);  // flaky, slow
```

## Common Patterns

### Forms
```javascript
await page.getByLabel('Email').fill('user@test.com');
await page.getByLabel('Password').fill('secret');
await page.getByRole('button', { name: /submit/i }).click();
```

### Dropdowns (Select)
```javascript
await page.getByLabel('Country').selectOption('US');
// or for custom dropdowns:
await page.getByRole('combobox').click();
await page.getByRole('option', { name: 'United States' }).click();
```

### Tables
```javascript
const row = page.getByRole('row').filter({ hasText: 'John Doe' });
await row.getByRole('button', { name: 'Edit' }).click();
```

### Iframes
```javascript
const frame = page.frameLocator('#payment-iframe');
await frame.getByLabel('Card number').fill('4242424242424242');
```

## Debugging Selectors

```javascript
// Highlight matching elements (headed mode)
await page.locator('.my-selector').highlight();

// Count matches
const count = await page.getByRole('listitem').count();

// Get all matching text contents
const texts = await page.getByRole('listitem').allTextContents();

// Use Playwright Inspector
// Launch with: PWDEBUG=1 node run.js /tmp/test.js
```

## Anti-Patterns

- Avoid `page.click()` / `page.$()` -- use locator API instead
- Avoid `waitForTimeout()` -- use condition-based waits
- Avoid complex CSS selectors -- prefer role/label selectors
- Avoid XPath unless no alternative exists
- Never rely on auto-generated class names (e.g., `css-1a2b3c`)
