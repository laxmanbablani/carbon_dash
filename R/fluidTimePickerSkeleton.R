# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fluidTimePickerSkeleton <- function(children=NULL, id=NULL, className=NULL, isOnlyTwo=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, isOnlyTwo=isOnlyTwo, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FluidTimePickerSkeleton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'isOnlyTwo', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
