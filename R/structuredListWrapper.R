# AUTO GENERATED FILE - DO NOT EDIT

#' @export
structuredListWrapper <- function(children=NULL, id=NULL, ariaLabel=NULL, className=NULL, isCondensed=NULL, isFlush=NULL, loading_state=NULL, selectedInitialRow=NULL, selection=NULL, style=NULL) {
    
    props <- list(children=children, id=id, ariaLabel=ariaLabel, className=className, isCondensed=isCondensed, isFlush=isFlush, loading_state=loading_state, selectedInitialRow=selectedInitialRow, selection=selection, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'StructuredListWrapper',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ariaLabel', 'className', 'isCondensed', 'isFlush', 'loading_state', 'selectedInitialRow', 'selection', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
