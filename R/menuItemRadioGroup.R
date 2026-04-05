# AUTO GENERATED FILE - DO NOT EDIT

#' @export
menuItemRadioGroup <- function(children=NULL, id=NULL, className=NULL, defaultSelectedItem=NULL, itemToString=NULL, items=NULL, label=NULL, loading_state=NULL, onChange=NULL, selectedItem=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultSelectedItem=defaultSelectedItem, itemToString=itemToString, items=items, label=label, loading_state=loading_state, onChange=onChange, selectedItem=selectedItem, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MenuItemRadioGroup',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'defaultSelectedItem', 'itemToString', 'items', 'label', 'loading_state', 'onChange', 'selectedItem', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
