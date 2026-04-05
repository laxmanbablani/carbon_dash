# AUTO GENERATED FILE - DO NOT EDIT

export formitem

"""
    formitem(;kwargs...)
    formitem(children::Any;kwargs...)
    formitem(children_maker::Function;kwargs...)


A FormItem component.
FormItem is a wrapper for the Carbon FormItem component.
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
function formitem(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("formitem", "FormItem", "carbon_dash", available_props, wild_props; kwargs...)
end

formitem(children::Any; kwargs...) = formitem(;kwargs..., children = children)
formitem(children_maker::Function; kwargs...) = formitem(children_maker(); kwargs...)

