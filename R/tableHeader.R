# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableHeader <- function(children=NULL, id=NULL, className=NULL, colSpan=NULL, isSortHeader=NULL, isSortable=NULL, loading_state=NULL, onClick=NULL, scope=NULL, sortDirection=NULL, style=NULL, translateWithId=NULL) {
    
    props <- list(children=children, id=id, className=className, colSpan=colSpan, isSortHeader=isSortHeader, isSortable=isSortable, loading_state=loading_state, onClick=onClick, scope=scope, sortDirection=sortDirection, style=style, translateWithId=translateWithId)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableHeader',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'colSpan', 'isSortHeader', 'isSortable', 'loading_state', 'onClick', 'scope', 'sortDirection', 'style', 'translateWithId'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
