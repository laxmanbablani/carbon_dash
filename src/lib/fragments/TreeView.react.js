import React from 'react';
import { TreeView as CarbonTreeView } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const TreeView = (props) => {
    const {
        id,
        setProps,
        children,
        className = '',
        loading_state,
        style,
        selected = null,
        active = null,
        ...otherProps
    } = props;
    const onSelect = (...args) => {
        if (setProps) {
            setProps({
                active: (args[1] && (args[1].activeNodeId || args[1].nodeId || args[1].id)) || args[0],
            });
        }
    };

    return (
        <CarbonTreeView
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            selected={selected}
            active={active}
            onSelect={onSelect}
            {...otherProps}
        >
            {children}
        </CarbonTreeView>
    );
};

export default TreeView;
