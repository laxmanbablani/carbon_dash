# AUTO GENERATED FILE - DO NOT EDIT

export uishell

"""
    uishell(;kwargs...)
    uishell(children::Any;kwargs...)
    uishell(children_maker::Function;kwargs...)


An UIShell component.
UIShell is a wrapper for the Carbon UIShell component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the component.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Specify a custom className to be applied to the component.
"""
function uishell(; kwargs...)
        available_props = Symbol[:children, :id, :className]
        wild_props = Symbol[]
        return Component("uishell", "UIShell", "carbon_dash", available_props, wild_props; kwargs...)
end

uishell(children::Any; kwargs...) = uishell(;kwargs..., children = children)
uishell(children_maker::Function; kwargs...) = uishell(children_maker(); kwargs...)

