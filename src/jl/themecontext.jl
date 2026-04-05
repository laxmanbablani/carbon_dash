# AUTO GENERATED FILE - DO NOT EDIT

export themecontext

"""
    themecontext(;kwargs...)
    themecontext(children::Any;kwargs...)
    themecontext(children_maker::Function;kwargs...)


A ThemeContext component.
ThemeContext is a wrapper for the Carbon ThemeContext component.
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
function themecontext(; kwargs...)
        available_props = Symbol[:children, :id, :className, :loading_state, :style]
        wild_props = Symbol[]
        return Component("themecontext", "ThemeContext", "carbon_dash", available_props, wild_props; kwargs...)
end

themecontext(children::Any; kwargs...) = themecontext(;kwargs..., children = children)
themecontext(children_maker::Function; kwargs...) = themecontext(children_maker(); kwargs...)

