import React from 'react';
import { FileUploaderDropContainer as CarbonFileUploaderDropContainer } from '@carbon/react';

const FileUploaderDropContainer = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        
        ...otherProps
    } = props;
    return (
        <CarbonFileUploaderDropContainer
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
