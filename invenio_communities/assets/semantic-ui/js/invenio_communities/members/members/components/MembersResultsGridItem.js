/*
 * This file is part of Invenio.
 * Copyright (C) 2022 CERN.
 *
 * Invenio is free software; you can redistribute it and/or modify it
 * under the terms of the MIT License; see LICENSE file for more details.
 */

import React from "react";
import { Card } from "semantic-ui-react";
import _truncate from "lodash/truncate";
import _upperFirst from "lodash/upperFirst";

export function MembersResultsGridItem({ result, index }) {
  return (
    <Card fluid key={index} href={`/members/${result.id}`}>
      <Card.Content>
        <Card.Header>{result.member.name}</Card.Header>
        <Card.Description>
          <div
            className="truncate-lines-1"
            dangerouslySetInnerHTML={{
              __html: result.member.description,
            }}
          />
        </Card.Description>
      </Card.Content>
    </Card>
  );
}