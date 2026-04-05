# AUTO GENERATED FILE - DO NOT EDIT

export contextmenu

"""
    contextmenu(;kwargs...)
    contextmenu(children::Any;kwargs...)
    contextmenu(children_maker::Function;kwargs...)


A ContextMenu component.
ContextMenu is a wrapper for the Carbon ContextMenu component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function contextmenu(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("contextmenu", "ContextMenu", "carbon_dash", available_props, wild_props; kwargs...)
end

contextmenu(children::Any; kwargs...) = contextmenu(;kwargs..., children = children)
contextmenu(children_maker::Function; kwargs...) = contextmenu(children_maker(); kwargs...)

