# AUTO GENERATED FILE - DO NOT EDIT

export definitiontooltip

"""
    definitiontooltip(;kwargs...)
    definitiontooltip(children::Any;kwargs...)
    definitiontooltip(children_maker::Function;kwargs...)


A DefinitionTooltip component.
DefinitionTooltip is a wrapper for the Carbon DefinitionTooltip component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `align` (Bool | Real | String | Dict | Array; optional): align
- `autoAlign` (Bool | Real | String | Dict | Array; optional): autoAlign
- `className` (String; optional): className
- `defaultOpen` (Bool | Real | String | Dict | Array; optional): defaultOpen
- `definition` (Bool | Real | String | Dict | Array; optional): definition
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `openOnHover` (Bool | Real | String | Dict | Array; optional): openOnHover
- `style` (Dict; optional): style
- `tooltipText` (Bool | Real | String | Dict | Array; optional): tooltipText
- `triggerClassName` (Bool | Real | String | Dict | Array; optional): triggerClassName
"""
function definitiontooltip(; kwargs...)
        available_props = Symbol[:children, :id, :align, :autoAlign, :className, :defaultOpen, :definition, :loading_state, :openOnHover, :style, :tooltipText, :triggerClassName]
        wild_props = Symbol[]
        return Component("definitiontooltip", "DefinitionTooltip", "carbon_dash", available_props, wild_props; kwargs...)
end

definitiontooltip(children::Any; kwargs...) = definitiontooltip(;kwargs..., children = children)
definitiontooltip(children_maker::Function; kwargs...) = definitiontooltip(children_maker(); kwargs...)

