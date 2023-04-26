import { useState } from "react";
import { DragDropContext, Droppable, Draggable } from "react-beautiful-dnd";

const Grid = () => {
  const [items, setItems] = useState([
    { id: "item-1", text: "Item 1" },
    { id: "item-2", text: "Item 2" },
    { id: "item-3", text: "Item 3" },
    { id: "item-4", text: "Item 4" },
    { id: "item-5", text: "Item 5" },
  ]);

  const onDragEnd = (result) => {
    if (!result.destination) {
      return;
    }

    const startIndex = result.source.index;
    const endIndex = result.destination.index;

    const [removed] = items.splice(startIndex, 1);
    items.splice(endIndex, 0, removed);

    setItems([...items]);
  };

  return (
    <DragDropContext onDragEnd={onDragEnd}>
      <Droppable droppableId="grid">
        {(provided) => (
          <div {...provided.droppableProps} ref={provided.innerRef} className="grid">
            {items.map(({ id, text }, index) => (
              <Draggable key={id} draggableId={id} index={index}>
                {(provided) => (
                  <div
                    {...provided.draggableProps}
                    {...provided.dragHandleProps}
                    ref={provided.innerRef}
                    className="item"
                  >
                    {text}
                  </div>
                )}
              </Draggable>
            ))}
            {provided.placeholder}
          </div>
        )}
      </Droppable>
    </DragDropContext>
  );
};

export default Grid;
