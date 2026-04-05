# AUTO GENERATED FILE - DO NOT EDIT

export fluidtextinputskeleton

"""
    fluidtextinputskeleton(;kwargs...)
    fluidtextinputskeleton(children::Any;kwargs...)
    fluidtextinputskeleton(children_maker::Function;kwargs...)


A FluidTextInputSkeleton component.
FluidTextInputSkeleton is a wrapper for the Carbon FluidTextInputSkeleton component.
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
function fluidtextinputskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("fluidtextinputskeleton", "FluidTextInputSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

fluidtextinputskeleton(children::Any; kwargs...) = fluidtextinputskeleton(;kwargs..., children = children)
fluidtextinputskeleton(children_maker::Function; kwargs...) = fluidtextinputskeleton(children_maker(); kwargs...)

