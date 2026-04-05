import React from 'react';
import { FileUploaderDropContainer as CarbonFileUploaderDropContainer } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const FileUploaderDropContainer = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFileUploaderDropContainer
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            
            {...otherProps}
        >
            {children}
        </CarbonFileUploaderDropContainer>
    );
};

export default FileUploaderDropContainer;
