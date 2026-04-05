# AUTO GENERATED FILE - DO NOT EDIT

#' @export
unorderedList <- function(children=NULL, id=NULL, className=NULL, isExpressive=NULL, loading_state=NULL, nested=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, isExpressive=isExpressive, loading_state=loading_state, nested=nested, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'UnorderedList',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'isExpressive', 'loading_state', 'nested', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
