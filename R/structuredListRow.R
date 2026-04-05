# AUTO GENERATED FILE - DO NOT EDIT

#' @export
structuredListRow <- function(children=NULL, id=NULL, className=NULL, head=NULL, label=NULL, loading_state=NULL, onClick=NULL, onKeyDown=NULL, selection=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, head=head, label=label, loading_state=loading_state, onClick=onClick, onKeyDown=onKeyDown, selection=selection, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'StructuredListRow',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'head', 'label', 'loading_state', 'onClick', 'onKeyDown', 'selection', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
