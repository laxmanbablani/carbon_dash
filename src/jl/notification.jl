# AUTO GENERATED FILE - DO NOT EDIT

export notification

"""
    notification(;kwargs...)
    notification(children::Any;kwargs...)
    notification(children_maker::Function;kwargs...)


A Notification component.
Notification is a wrapper for the Carbon Notification component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function notification(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("notification", "Notification", "carbon_dash", available_props, wild_props; kwargs...)
end

notification(children::Any; kwargs...) = notification(;kwargs..., children = children)
notification(children_maker::Function; kwargs...) = notification(children_maker(); kwargs...)

