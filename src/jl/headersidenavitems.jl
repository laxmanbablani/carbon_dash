# AUTO GENERATED FILE - DO NOT EDIT

export headersidenavitems

"""
    headersidenavitems(;kwargs...)
    headersidenavitems(children::Any;kwargs...)
    headersidenavitems(children_maker::Function;kwargs...)


A HeaderSideNavItems component.
HeaderSideNavItems is a wrapper for the Carbon HeaderSideNavItems component.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): children
- `id` (String; optional): id
- `className` (String; optional): className
- `hasDivider` (Bool | Real | String | Dict | Array; optional): hasDivider
- `loading_state` (optional): loading_state. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional)
  - `prop_name` (String; optional)
  - `component_name` (String; optional)
- `style` (Dict; optional): style
"""
function headersidenavitems(; kwargs...)
        available_props = Symbol[:children, :id, :className, :hasDivider, :loading_state, :style]
        wild_props = Symbol[]
        return Component("headersidenavitems", "HeaderSideNavItems", "carbon_dash", available_props, wild_props; kwargs...)
end

headersidenavitems(children::Any; kwargs...) = headersidenavitems(;kwargs..., children = children)
headersidenavitems(children_maker::Function; kwargs...) = headersidenavitems(children_maker(); kwargs...)

