# AUTO GENERATED FILE - DO NOT EDIT

#' @export
structuredListCell <- function(children=NULL, id=NULL, className=NULL, head=NULL, loading_state=NULL, noWrap=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, head=head, loading_state=loading_state, noWrap=noWrap, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'StructuredListCell',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'head', 'loading_state', 'noWrap', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
