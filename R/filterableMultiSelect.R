# AUTO GENERATED FILE - DO NOT EDIT

#' @export
filterableMultiSelect <- function(children=NULL, id=NULL, ariaLabel=NULL, autoAlign=NULL, className=NULL, clearSelectionDescription=NULL, clearSelectionText=NULL, compareItems=NULL, decorator=NULL, direction=NULL, disabled=NULL, downshiftProps=NULL, filterItems=NULL, hideLabel=NULL, initialSelectedItems=NULL, inputProps=NULL, invalid=NULL, invalidText=NULL, itemToElement=NULL, itemToString=NULL, items=NULL, light=NULL, loading_state=NULL, locale=NULL, onChange=NULL, onInputValueChange=NULL, onMenuChange=NULL, open=NULL, placeholder=NULL, selectionFeedback=NULL, size=NULL, slug=NULL, sortItems=NULL, style=NULL, titleText=NULL, translateWithId=NULL, type=NULL, useTitleInItem=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, ariaLabel=ariaLabel, autoAlign=autoAlign, className=className, clearSelectionDescription=clearSelectionDescription, clearSelectionText=clearSelectionText, compareItems=compareItems, decorator=decorator, direction=direction, disabled=disabled, downshiftProps=downshiftProps, filterItems=filterItems, hideLabel=hideLabel, initialSelectedItems=initialSelectedItems, inputProps=inputProps, invalid=invalid, invalidText=invalidText, itemToElement=itemToElement, itemToString=itemToString, items=items, light=light, loading_state=loading_state, locale=locale, onChange=onChange, onInputValueChange=onInputValueChange, onMenuChange=onMenuChange, open=open, placeholder=placeholder, selectionFeedback=selectionFeedback, size=size, slug=slug, sortItems=sortItems, style=style, titleText=titleText, translateWithId=translateWithId, type=type, useTitleInItem=useTitleInItem, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FilterableMultiSelect',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ariaLabel', 'autoAlign', 'className', 'clearSelectionDescription', 'clearSelectionText', 'compareItems', 'decorator', 'direction', 'disabled', 'downshiftProps', 'filterItems', 'hideLabel', 'initialSelectedItems', 'inputProps', 'invalid', 'invalidText', 'itemToElement', 'itemToString', 'items', 'light', 'loading_state', 'locale', 'onChange', 'onInputValueChange', 'onMenuChange', 'open', 'placeholder', 'selectionFeedback', 'size', 'slug', 'sortItems', 'style', 'titleText', 'translateWithId', 'type', 'useTitleInItem', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
