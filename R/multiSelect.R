# AUTO GENERATED FILE - DO NOT EDIT

#' @export
multiSelect <- function(children=NULL, id=NULL, autoAlign=NULL, className=NULL, clearSelectionDescription=NULL, clearSelectionText=NULL, compareItems=NULL, decorator=NULL, direction=NULL, disabled=NULL, downshiftProps=NULL, helperText=NULL, hideLabel=NULL, initialSelectedItems=NULL, invalid=NULL, invalidText=NULL, itemToElement=NULL, itemToString=NULL, items=NULL, label=NULL, light=NULL, loading_state=NULL, locale=NULL, onChange=NULL, onMenuChange=NULL, open=NULL, readOnly=NULL, selectedItems=NULL, selectionFeedback=NULL, size=NULL, slug=NULL, sortItems=NULL, style=NULL, titleText=NULL, translateWithId=NULL, type=NULL, useTitleInItem=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, autoAlign=autoAlign, className=className, clearSelectionDescription=clearSelectionDescription, clearSelectionText=clearSelectionText, compareItems=compareItems, decorator=decorator, direction=direction, disabled=disabled, downshiftProps=downshiftProps, helperText=helperText, hideLabel=hideLabel, initialSelectedItems=initialSelectedItems, invalid=invalid, invalidText=invalidText, itemToElement=itemToElement, itemToString=itemToString, items=items, label=label, light=light, loading_state=loading_state, locale=locale, onChange=onChange, onMenuChange=onMenuChange, open=open, readOnly=readOnly, selectedItems=selectedItems, selectionFeedback=selectionFeedback, size=size, slug=slug, sortItems=sortItems, style=style, titleText=titleText, translateWithId=translateWithId, type=type, useTitleInItem=useTitleInItem, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MultiSelect',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'autoAlign', 'className', 'clearSelectionDescription', 'clearSelectionText', 'compareItems', 'decorator', 'direction', 'disabled', 'downshiftProps', 'helperText', 'hideLabel', 'initialSelectedItems', 'invalid', 'invalidText', 'itemToElement', 'itemToString', 'items', 'label', 'light', 'loading_state', 'locale', 'onChange', 'onMenuChange', 'open', 'readOnly', 'selectedItems', 'selectionFeedback', 'size', 'slug', 'sortItems', 'style', 'titleText', 'translateWithId', 'type', 'useTitleInItem', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
