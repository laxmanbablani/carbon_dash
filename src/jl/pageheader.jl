# AUTO GENERATED FILE - DO NOT EDIT

export pageheader

"""
    pageheader(;kwargs...)
    pageheader(children::Any;kwargs...)
    pageheader(children_maker::Function;kwargs...)


A PageHeader component.
PageHeader is a wrapper for the Carbon PageHeader component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function pageheader(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("pageheader", "PageHeader", "carbon_dash", available_props, wild_props; kwargs...)
end

pageheader(children::Any; kwargs...) = pageheader(;kwargs..., children = children)
pageheader(children_maker::Function; kwargs...) = pageheader(children_maker(); kwargs...)

