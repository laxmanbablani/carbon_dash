# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fluidMultiSelect <- function(children=NULL, id=NULL, className=NULL, clearSelectionDescription=NULL, clearSelectionText=NULL, compareItems=NULL, direction=NULL, disabled=NULL, downshiftProps=NULL, initialSelectedItems=NULL, invalid=NULL, invalidText=NULL, isCondensed=NULL, isFilterable=NULL, itemToElement=NULL, itemToString=NULL, items=NULL, label=NULL, loading_state=NULL, locale=NULL, onChange=NULL, onInputValueChange=NULL, onMenuChange=NULL, readOnly=NULL, selectedItems=NULL, selectionFeedback=NULL, sortItems=NULL, style=NULL, titleText=NULL, translateWithId=NULL, useTitleInItem=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, clearSelectionDescription=clearSelectionDescription, clearSelectionText=clearSelectionText, compareItems=compareItems, direction=direction, disabled=disabled, downshiftProps=downshiftProps, initialSelectedItems=initialSelectedItems, invalid=invalid, invalidText=invalidText, isCondensed=isCondensed, isFilterable=isFilterable, itemToElement=itemToElement, itemToString=itemToString, items=items, label=label, loading_state=loading_state, locale=locale, onChange=onChange, onInputValueChange=onInputValueChange, onMenuChange=onMenuChange, readOnly=readOnly, selectedItems=selectedItems, selectionFeedback=selectionFeedback, sortItems=sortItems, style=style, titleText=titleText, translateWithId=translateWithId, useTitleInItem=useTitleInItem, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FluidMultiSelect',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'clearSelectionDescription', 'clearSelectionText', 'compareItems', 'direction', 'disabled', 'downshiftProps', 'initialSelectedItems', 'invalid', 'invalidText', 'isCondensed', 'isFilterable', 'itemToElement', 'itemToString', 'items', 'label', 'loading_state', 'locale', 'onChange', 'onInputValueChange', 'onMenuChange', 'readOnly', 'selectedItems', 'selectionFeedback', 'sortItems', 'style', 'titleText', 'translateWithId', 'useTitleInItem', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
