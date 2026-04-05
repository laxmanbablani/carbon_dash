# AUTO GENERATED FILE - DO NOT EDIT

export fluidcomboboxskeleton

"""
    fluidcomboboxskeleton(;kwargs...)
    fluidcomboboxskeleton(children::Any;kwargs...)
    fluidcomboboxskeleton(children_maker::Function;kwargs...)


A FluidComboBoxSkeleton component.
FluidComboBoxSkeleton is a wrapper for the Carbon FluidComboBoxSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function fluidcomboboxskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("fluidcomboboxskeleton", "FluidComboBoxSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidcomboboxskeleton(children::Any; kwargs...) = fluidcomboboxskeleton(;kwargs..., children = children)
fluidcomboboxskeleton(children_maker::Function; kwargs...) = fluidcomboboxskeleton(children_maker(); kwargs...)

