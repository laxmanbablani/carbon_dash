# AUTO GENERATED FILE - DO NOT EDIT

export dropdownskeleton

"""
    dropdownskeleton(;kwargs...)
    dropdownskeleton(children::Any;kwargs...)
    dropdownskeleton(children_maker::Function;kwargs...)


A DropdownSkeleton component.
DropdownSkeleton is a wrapper for the Carbon DropdownSkeleton component.
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
- `size` (Bool | Real | String | Dict | Array; optional): size
- `style` (Dict; optional): style
"""
function dropdownskeleton(; kwargs...)
        available_props = Symbol[:children, :id, :className, :hideLabel, :loading_state, :size, :style]
        wild_props = Symbol[]
        return Component("dropdownskeleton", "DropdownSkeleton", "carbon_dash", available_props, wild_props; kwargs...)
end

dropdownskeleton(children::Any; kwargs...) = dropdownskeleton(;kwargs..., children = children)
dropdownskeleton(children_maker::Function; kwargs...) = dropdownskeleton(children_maker(); kwargs...)

