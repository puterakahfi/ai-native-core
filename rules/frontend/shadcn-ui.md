# shadcn/ui Frontend Rule

## Purpose

Ensure frontend output is consistent, maintainable, accessible, and aligned with a reusable design system.

## Applies To

- Next.js applications
- React components
- Internal tools
- SaaS dashboards
- Product UI
- ExampleProduct UI

## Must Do

1. Use shadcn/ui as the base component system when the Engineering Contract specifies it.
2. Compose UI from reusable components instead of one-off markup.
3. Use Tailwind CSS tokens consistently.
4. Keep layout, typography, spacing, and interaction patterns consistent.
5. Ensure mobile readability.
6. Respect accessibility basics: labels, focus states, keyboard navigation, contrast, and semantic HTML.
7. Keep feature-specific UI inside the feature/module boundary.
8. Use loading, empty, error, and success states.

## Must Not Do

1. Do not create random component styles outside the design system.
2. Do not hardcode inconsistent spacing, font sizes, or colors everywhere.
3. Do not overload cards and dashboards with too many visual elements.
4. Do not create UI that looks like a generic AI-generated template.
5. Do not skip responsive behavior.
6. Do not hide critical actions without clear affordance.

## UI Quality Rules

Every major screen should define:

```text
- Main user goal
- Primary action
- Secondary actions
- Status state
- Empty state
- Error state
- Review/approval state when relevant
```

## Review Checklist

- [ ] Uses shadcn/ui components where appropriate.
- [ ] Typography hierarchy is clear.
- [ ] Spacing is consistent.
- [ ] Primary action is obvious.
- [ ] Empty/error/loading states exist.
- [ ] Mobile layout is readable.
- [ ] UI supports the product workflow state.
- [ ] Design does not feel random or AI-generated.

## ExampleProduct Example

ExampleProduct should use premium editorial SaaS direction:

```text
- Off-white or neutral background
- Dark text
- Muted accent color
- Fewer cards
- Generous whitespace
- Realistic product UI previews
- Strong visual hierarchy
- No neon-heavy AI aesthetic by default
```
