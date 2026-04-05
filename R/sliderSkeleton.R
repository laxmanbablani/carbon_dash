# AUTO GENERATED FILE - DO NOT EDIT

#' @export
sliderSkeleton <- function(children=NULL, id=NULL, ariaLabel=NULL, className=NULL, hideLabel=NULL, loading_state=NULL, style=NULL, twoHandles=NULL, unstable_ariaLabelHandleUpper=NULL) {
    
    props <- list(children=children, id=id, ariaLabel=ariaLabel, className=className, hideLabel=hideLabel, loading_state=loading_state, style=style, twoHandles=twoHandles, unstable_ariaLabelHandleUpper=unstable_ariaLabelHandleUpper)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SliderSkeleton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ariaLabel', 'className', 'hideLabel', 'loading_state', 'style', 'twoHandles', 'unstable_ariaLabelHandleUpper'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
