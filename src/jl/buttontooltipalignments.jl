# AUTO GENERATED FILE - DO NOT EDIT

export buttontooltipalignments

"""
    buttontooltipalignments(;kwargs...)
    buttontooltipalignments(children::Any;kwargs...)
    buttontooltipalignments(children_maker::Function;kwargs...)


A ButtonTooltipAlignments component.
ButtonTooltipAlignments is a wrapper for the Carbon ButtonTooltipAlignments component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
- `style` (Dict; optional): Inline styles
"""
function buttontooltipalignments(; kwargs...)
        available_props = Symbol[:children, :id, :className, :style]
        wild_props = Symbol[]
        return Component("buttontooltipalignments", "ButtonTooltipAlignments", "carbon_dash", available_props, wild_props; kwargs...)
end

buttontooltipalignments(children::Any; kwargs...) = buttontooltipalignments(;kwargs..., children = children)
buttontooltipalignments(children_maker::Function; kwargs...) = buttontooltipalignments(children_maker(); kwargs...)

