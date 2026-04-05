# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableToolbarSearch <- function(children=NULL, id=NULL, className=NULL, defaultExpanded=NULL, defaultValue=NULL, disabled=NULL, expanded=NULL, labelText=NULL, loading_state=NULL, onBlur=NULL, onChange=NULL, onClear=NULL, onExpand=NULL, onFocus=NULL, persistent=NULL, placeholder=NULL, searchContainerClass=NULL, size=NULL, style=NULL, tabIndex=NULL, translateWithId=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultExpanded=defaultExpanded, defaultValue=defaultValue, disabled=disabled, expanded=expanded, labelText=labelText, loading_state=loading_state, onBlur=onBlur, onChange=onChange, onClear=onClear, onExpand=onExpand, onFocus=onFocus, persistent=persistent, placeholder=placeholder, searchContainerClass=searchContainerClass, size=size, style=style, tabIndex=tabIndex, translateWithId=translateWithId)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableToolbarSearch',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'defaultExpanded', 'defaultValue', 'disabled', 'expanded', 'labelText', 'loading_state', 'onBlur', 'onChange', 'onClear', 'onExpand', 'onFocus', 'persistent', 'placeholder', 'searchContainerClass', 'size', 'style', 'tabIndex', 'translateWithId'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
