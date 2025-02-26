class SimpleDB:
    def __init__(self):
        self.main_map = {}
        self.transaction_stack = []

    def set(self, key, value):
        """sets the value associated with the key"""
        if self.transaction_stack:
            temp_map = self.transaction_stack[-1]
            temp_map[key] = value
        else:
            self.main_map[key] = value

    def get(self, key):
        """
        get returns the value associated with the key
        get should raise a KeyError if the key doesn't exist
        """
        if self.transaction_stack:
            curr_map = self.transaction_stack[-1]
        else:
            curr_map = self.main_map
        
        if key not in curr_map or curr_map[key] is None:
            raise KeyError('Key not found')
        else:
            return curr_map[key]

    def unset(self, key):
        """unset should delete the key from the db"""
        
        if self.transaction_stack:
            currMap = self.transaction_stack[-1]
            if key not in currMap:
                raise KeyError("key not found")

            self.transaction_stack[-1][key] = None
        else:
            currMap = self.main_map
            if key not in currMap:
                raise KeyError("key not found")
            
            del self.main_map[key]

    def begin(self):
        """begin starts a new transaction"""
        if self.transaction_stack:
            new_map = self.transaction_stack[-1].copy()
        else:
            new_map = self.main_map.copy()

        self.transaction_stack.append(new_map)

    def commit(self):
        """
        commit applies all transactions
        it should raise an Exception if there is no ongoing transaction
        """
        if not self.transaction_stack:
            raise Exception('No ongoing transaction')

        last_transaction_map = self.transaction_stack.pop()
        self.transaction_stack = []

        for key, value in last_transaction_map.items():
            if value is None:
                del self.main_map[key]
            else:
                self.main_map[key] = value
        

    def rollback(self):
        """
        rollback undoes the most recent transaction
        it should raise an Exception if there is no ongoing transaction
        """
        if self.transaction_stack:
            self.transaction_stack.pop()
        else:
            raise Exception("No ongoing transaction")
