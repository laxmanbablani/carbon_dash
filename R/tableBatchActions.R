# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableBatchActions <- function(children=NULL, id=NULL, className=NULL, loading_state=NULL, onCancel=NULL, onSelectAll=NULL, shouldShowBatchActions=NULL, style=NULL, totalCount=NULL, totalSelected=NULL, translateWithId=NULL) {
    
    props <- list(children=children, id=id, className=className, loading_state=loading_state, onCancel=onCancel, onSelectAll=onSelectAll, shouldShowBatchActions=shouldShowBatchActions, style=style, totalCount=totalCount, totalSelected=totalSelected, translateWithId=translateWithId)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableBatchActions',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'loading_state', 'onCancel', 'onSelectAll', 'shouldShowBatchActions', 'style', 'totalCount', 'totalSelected', 'translateWithId'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
