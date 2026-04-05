# AUTO GENERATED FILE - DO NOT EDIT

export textinputskeleton

"""
    textinputskeleton(;kwargs...)
    textinputskeleton(children::Any;kwargs...)
    textinputskeleton(children_maker::Function;kwargs...)


A TextInputSkeleton component.
TextInputSkeleton is a wrapper for the Carbon TextInputSkeleton component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `hideLabel` (Bool | Real | String | Dict | Array; optional): hideLabel
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function textinputskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :hideLabel, :loading_state, :style]
        wild_props = Symbol[]
        return Component("textinputskeleton", "TextInputSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

textinputskeleton(children::Any; kwargs...) = textinputskeleton(;kwargs..., children = children)
textinputskeleton(children_maker::Function; kwargs...) = textinputskeleton(children_maker(); kwargs...)

