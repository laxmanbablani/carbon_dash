# AUTO GENERATED FILE - DO NOT EDIT

export listbox

"""
    listbox(;kwargs...)
    listbox(children::Any;kwargs...)
    listbox(children_maker::Function;kwargs...)


A ListBox component.
ListBox is a wrapper for the Carbon ListBox component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function listbox(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("listbox", "ListBox", "carbon_dash", available_props, wild_props; kwargs...)
end

listbox(children::Any; kwargs...) = listbox(;kwargs..., children = children)
listbox(children_maker::Function; kwargs...) = listbox(children_maker(); kwargs...)

