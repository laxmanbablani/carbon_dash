# AUTO GENERATED FILE - DO NOT EDIT

#' @export
paginationNav <- function(children=NULL, id=NULL, className=NULL, disableOverflow=NULL, itemsShown=NULL, loading_state=NULL, loop=NULL, onChange=NULL, page=NULL, size=NULL, style=NULL, tooltipAlignment=NULL, tooltipPosition=NULL, totalItems=NULL, translateWithId=NULL) {
    
    props <- list(children=children, id=id, className=className, disableOverflow=disableOverflow, itemsShown=itemsShown, loading_state=loading_state, loop=loop, onChange=onChange, page=page, size=size, style=style, tooltipAlignment=tooltipAlignment, tooltipPosition=tooltipPosition, totalItems=totalItems, translateWithId=translateWithId)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'PaginationNav',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'disableOverflow', 'itemsShown', 'loading_state', 'loop', 'onChange', 'page', 'size', 'style', 'tooltipAlignment', 'tooltipPosition', 'totalItems', 'translateWithId'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
