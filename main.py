from Core.state_manager import StateManager
from Utilities.file_manager import FileManager
from Utilities.display import Display

def main():
    
    save_id=''
    
    if save_id == '':
        state_manager = StateManager()
        FileManager.save(state_manager.history)
        print(f'New Game: {state_manager.history.save_id}')
    else:
        loaded_history = FileManager.load(save_id)
        state_manager = StateManager(loaded_history)
        print(f'Loaded Game: {state_manager.history.save_id}')

    current_state = state_manager.get_current_state()
    Display.draw_state(state=current_state, grid=state_manager.history.grid)

if __name__ == '__main__':
    main()