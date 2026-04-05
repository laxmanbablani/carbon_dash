# AUTO GENERATED FILE - DO NOT EDIT

#' @export
composedModal <- function(children=NULL, id=NULL, className=NULL, containerClassName=NULL, current=NULL, danger=NULL, decorator=NULL, isFullWidth=NULL, launcherButtonRef=NULL, loading_state=NULL, onClose=NULL, onKeyDown=NULL, open=NULL, preventCloseOnClickOutside=NULL, selectorPrimaryFocus=NULL, selectorsFloatingMenus=NULL, size=NULL, slug=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, containerClassName=containerClassName, current=current, danger=danger, decorator=decorator, isFullWidth=isFullWidth, launcherButtonRef=launcherButtonRef, loading_state=loading_state, onClose=onClose, onKeyDown=onKeyDown, open=open, preventCloseOnClickOutside=preventCloseOnClickOutside, selectorPrimaryFocus=selectorPrimaryFocus, selectorsFloatingMenus=selectorsFloatingMenus, size=size, slug=slug, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ComposedModal',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'containerClassName', 'current', 'danger', 'decorator', 'isFullWidth', 'launcherButtonRef', 'loading_state', 'onClose', 'onKeyDown', 'open', 'preventCloseOnClickOutside', 'selectorPrimaryFocus', 'selectorsFloatingMenus', 'size', 'slug', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
