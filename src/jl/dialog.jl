# AUTO GENERATED FILE - DO NOT EDIT

export dialog

"""
    dialog(;kwargs...)
    dialog(children::Any;kwargs...)
    dialog(children_maker::Function;kwargs...)


A Dialog component.
Dialog is a wrapper for the Carbon Dialog component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function dialog(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("dialog", "Dialog", "carbon_dash", available_props, wild_props; kwargs...)
end

dialog(children::Any; kwargs...) = dialog(;kwargs..., children = children)
dialog(children_maker::Function; kwargs...) = dialog(children_maker(); kwargs...)

