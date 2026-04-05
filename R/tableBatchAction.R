# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableBatchAction <- function(children=NULL, id=NULL, className=NULL, hasIconOnly=NULL, iconDescription=NULL, loading_state=NULL, renderIcon=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, hasIconOnly=hasIconOnly, iconDescription=iconDescription, loading_state=loading_state, renderIcon=renderIcon, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableBatchAction',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'hasIconOnly', 'iconDescription', 'loading_state', 'renderIcon', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
