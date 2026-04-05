# AUTO GENERATED FILE - DO NOT EDIT

export overflowmenuv2

"""
    overflowmenuv2(;kwargs...)
    overflowmenuv2(children::Any;kwargs...)
    overflowmenuv2(children_maker::Function;kwargs...)


An OverflowMenuV2 component.
OverflowMenuV2 is a wrapper for the Carbon OverflowMenuV2 component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function overflowmenuv2(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("overflowmenuv2", "OverflowMenuV2", "carbon_dash", available_props, wild_props; kwargs...)
end

overflowmenuv2(children::Any; kwargs...) = overflowmenuv2(;kwargs..., children = children)
overflowmenuv2(children_maker::Function; kwargs...) = overflowmenuv2(children_maker(); kwargs...)

