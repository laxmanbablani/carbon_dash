# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dataTableSkeleton <- function(children=NULL, id=NULL, className=NULL, columnCount=NULL, headers=NULL, loading_state=NULL, rowCount=NULL, showHeader=NULL, showToolbar=NULL, size=NULL, style=NULL, zebra=NULL) {
    
    props <- list(children=children, id=id, className=className, columnCount=columnCount, headers=headers, loading_state=loading_state, rowCount=rowCount, showHeader=showHeader, showToolbar=showToolbar, size=size, style=style, zebra=zebra)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DataTableSkeleton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'columnCount', 'headers', 'loading_state', 'rowCount', 'showHeader', 'showToolbar', 'size', 'style', 'zebra'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
