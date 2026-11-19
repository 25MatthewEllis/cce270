# Concrete Slab Calculator — App Specification

## Purpose

Build a single-page app that estimates how much ready-mix concrete to order for
a rectangular slab and the material cost. The app is for planning; it does not
replace a contractor's or supplier's estimate.

## Inputs

| Input | Units | Range | Default | Control |
|---|---|---:|---:|---|
| Slab length | feet (ft) | 1–200 | 20 | Number input, step 0.1 |
| Slab width | feet (ft) | 1–200 | 10 | Number input, step 0.1 |
| Slab thickness | inches (in) | 1–24 | 4 | Number input, step 0.25 |
| Waste factor | percent (%) | 0–20 | 10 | Slider, step 1; show the current value |
| Concrete price | dollars per cubic yard ($/yd³) | $0–$1,000 | $175 | Number input, step $0.01 |

Show each input's label and units next to its control. The default price is an
editable example, not a quoted market price.

## Calculations

1. Convert thickness from inches to feet: `thickness_ft = thickness_in / 12`.
2. Calculate slab volume: `length_ft × width_ft × thickness_ft`.
3. Convert cubic feet to cubic yards by dividing by 27.
4. Apply waste: `volume_with_waste = slab_volume_yd³ × (1 + waste_percent / 100)`.
5. Round the order quantity **up** to the next quarter cubic yard:
   `order_quantity_yd³ = ceil(volume_with_waste × 4) / 4`.
6. Calculate estimated material cost using the rounded order quantity:
   `estimated_cost = order_quantity_yd³ × price_per_yd³`.

Do not round intermediate values. Display volume and order quantity to at most
two decimal places, and cost as currency to two decimal places.

## Outputs

- Show the concrete order quantity prominently in cubic yards, rounded up to
  the nearest 0.25 yd³.
- Show the estimated material cost prominently, based on the rounded order
  quantity.
- Also show the calculated slab volume before waste and the volume after waste
  but before order rounding, so the estimate is transparent.
- Show a simple rectangular slab diagram with length and width labeled and
  thickness called out. Treat it as a schematic, not a construction drawing.
- Recalculate all results and redraw/update the diagram immediately whenever
  an input changes.

## Validation and behavior

- Enforce each input's stated minimum, maximum, and step.
- Do not show misleading results when any input is empty, invalid, or outside
  its range; identify the input that needs correction.
- Keep calculation results in the stated units and clearly distinguish
  cubic yards from square feet and dollars per cubic yard from total cost.

## Look and feel

- Use a clear page title and a short explanation of what the estimate includes.
- On a wide screen, place the input controls in one column and the results and
  slab diagram in the adjacent column.
- On narrow screens, stack inputs, results, and diagram vertically.
- Keep units visible, use readable contrast, and make all controls usable by
  keyboard. Include a text alternative or equivalent dimension summary for
  the diagram.

## Scope

This is a single-file web app. Put the complete app in the root-level
`index.html` so it can be published with GitHub Pages. Do not add a backend,
account system, data persistence, or supplier-specific delivery fees.
