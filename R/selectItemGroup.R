# AUTO GENERATED FILE - DO NOT EDIT

#' @export
selectItemGroup <- function(children=NULL, id=NULL, className=NULL, disabled=NULL, label=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, disabled=disabled, label=label, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SelectItemGroup',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'disabled', 'label', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
