import React from 'react';
import * as Icons from '@carbon/react/icons';

export const resolveIcon = (iconProp) => {
    if (typeof iconProp === 'string' && Icons[iconProp]) {
        const IconComponent = Icons[iconProp];
        return <IconComponent />;
    }
    // Return as is if it's already a React element or not a string we recognize
    return iconProp;
};
