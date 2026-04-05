# AUTO GENERATED FILE - DO NOT EDIT

export inlinecheckbox

"""
    inlinecheckbox(;kwargs...)
    inlinecheckbox(children::Any;kwargs...)
    inlinecheckbox(children_maker::Function;kwargs...)


An InlineCheckbox component.
InlineCheckbox is a wrapper for the Carbon InlineCheckbox component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function inlinecheckbox(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("inlinecheckbox", "InlineCheckbox", "carbon_dash", available_props, wild_props; kwargs...)
end

inlinecheckbox(children::Any; kwargs...) = inlinecheckbox(;kwargs..., children = children)
inlinecheckbox(children_maker::Function; kwargs...) = inlinecheckbox(children_maker(); kwargs...)

