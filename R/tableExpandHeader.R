# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableExpandHeader <- function(children=NULL, id=NULL, ariaLabel=NULL, className=NULL, enableExpando=NULL, enableToggle=NULL, expandIconDescription=NULL, isExpanded=NULL, loading_state=NULL, onExpand=NULL, style=NULL) {
    
    props <- list(children=children, id=id, ariaLabel=ariaLabel, className=className, enableExpando=enableExpando, enableToggle=enableToggle, expandIconDescription=expandIconDescription, isExpanded=isExpanded, loading_state=loading_state, onExpand=onExpand, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableExpandHeader',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ariaLabel', 'className', 'enableExpando', 'enableToggle', 'expandIconDescription', 'isExpanded', 'loading_state', 'onExpand', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
