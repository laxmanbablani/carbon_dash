# AUTO GENERATED FILE - DO NOT EDIT

#' @export
inlineLoading <- function(children=NULL, id=NULL, className=NULL, description=NULL, iconDescription=NULL, loading_state=NULL, onSuccess=NULL, status=NULL, style=NULL, successDelay=NULL) {
    
    props <- list(children=children, id=id, className=className, description=description, iconDescription=iconDescription, loading_state=loading_state, onSuccess=onSuccess, status=status, style=style, successDelay=successDelay)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'InlineLoading',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'description', 'iconDescription', 'loading_state', 'onSuccess', 'status', 'style', 'successDelay'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
