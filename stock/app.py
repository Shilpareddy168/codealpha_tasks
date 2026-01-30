class StockPortfolio:
    """A class to manage and track a stock portfolio."""
    
    def __init__(self):
        # List to store all stocks (each stock is a dictionary)
        self.portfolio = []
    
    def add_stock(self, symbol, quantity, purchase_price):
        """Add a new stock to the portfolio."""
        stock = {
            'symbol': symbol.upper(),
            'quantity': quantity,
            'purchase_price': purchase_price,
            'current_price': purchase_price  # Initially set to purchase price
        }
        self.portfolio.append(stock)
        print(f"✓ Added {quantity} shares of {symbol.upper()} at ${purchase_price:.2f} per share")
    
    def remove_stock(self, symbol):
        """Remove a stock from the portfolio."""
        symbol = symbol.upper()
        for stock in self.portfolio:
            if stock['symbol'] == symbol:
                self.portfolio.remove(stock)
                print(f"✓ Removed {symbol} from portfolio")
                return
        print(f"✗ Stock {symbol} not found in portfolio")
    
    def update_price(self, symbol, new_price):
        """Update the current price of a stock."""
        symbol = symbol.upper()
        for stock in self.portfolio:
            if stock['symbol'] == symbol:
                stock['current_price'] = new_price
                print(f"✓ Updated {symbol} price to ${new_price:.2f}")
                return
        print(f"✗ Stock {symbol} not found in portfolio")
    
    def calculate_stock_value(self, stock):
        """Calculate the current value of a stock holding."""
        return stock['quantity'] * stock['current_price']
    
    def calculate_stock_gain_loss(self, stock):
        """Calculate profit/loss for a stock."""
        purchase_value = stock['quantity'] * stock['purchase_price']
        current_value = self.calculate_stock_value(stock)
        return current_value - purchase_value
    
    def calculate_stock_percentage(self, stock):
        """Calculate percentage gain/loss for a stock."""
        gain_loss = self.calculate_stock_gain_loss(stock)
        purchase_value = stock['quantity'] * stock['purchase_price']
        return (gain_loss / purchase_value) * 100
    
    def calculate_total_value(self):
        """Calculate total portfolio value."""
        total = 0
        for stock in self.portfolio:
            total += self.calculate_stock_value(stock)
        return total
    
    def calculate_total_investment(self):
        """Calculate total amount invested."""
        total = 0
        for stock in self.portfolio:
            total += stock['quantity'] * stock['purchase_price']
        return total
    
    def display_portfolio(self):
        """Display detailed portfolio information."""
        if not self.portfolio:
            print("\n📊 Your portfolio is empty!")
            return
        
        print("\n" + "=" * 100)
        print("📊 STOCK PORTFOLIO SUMMARY")
        print("=" * 100)
        print(f"{'Symbol':<10} {'Quantity':<10} {'Buy Price':<12} {'Current':<12} {'Value':<15} {'Gain/Loss':<15} {'Change %':<10}")
        print("-" * 100)
        
        for stock in self.portfolio:
            symbol = stock['symbol']
            quantity = stock['quantity']
            purchase_price = stock['purchase_price']
            current_price = stock['current_price']
            value = self.calculate_stock_value(stock)
            gain_loss = self.calculate_stock_gain_loss(stock)
            percentage = self.calculate_stock_percentage(stock)
            
            # Color coding for gains/losses
            sign = '+' if gain_loss >= 0 else ''
            
            print(f"{symbol:<10} {quantity:<10} ₹{purchase_price:<11.2f} ₹{current_price:<11.2f} ₹{value:<14.2f} {sign}₹{gain_loss:<13.2f} {sign}{percentage:<9.2f}%")
        
        print("-" * 100)
        
        # Portfolio totals
        total_investment = self.calculate_total_investment()
        total_value = self.calculate_total_value()
        total_gain_loss = total_value - total_investment
        total_percentage = (total_gain_loss / total_investment) * 100 if total_investment > 0 else 0
        
        print(f"\n{'Total Investment:':<30} ₹{total_investment:,.2f}")
        print(f"{'Current Portfolio Value:':<30} ₹{total_value:,.2f}")
        print(f"{'Total Gain/Loss:':<30} ₹{total_gain_loss:,.2f} ({total_percentage:+.2f}%)")
        print("=" * 100)
    
    def get_best_performer(self):
        """Find the stock with the highest percentage gain."""
        if not self.portfolio:
            return None
        
        best_stock = max(self.portfolio, key=lambda s: self.calculate_stock_percentage(s))
        return best_stock
    
    def get_worst_performer(self):
        """Find the stock with the lowest percentage gain."""
        if not self.portfolio:
            return None
        
        worst_stock = min(self.portfolio, key=lambda s: self.calculate_stock_percentage(s))
        return worst_stock
    
    def show_performance_summary(self):
        """Show best and worst performing stocks."""
        if not self.portfolio:
            print("\n📊 Your portfolio is empty!")
            return
        
        best = self.get_best_performer()
        worst = self.get_worst_performer()
        
        print("\n" + "=" * 60)
        print("🏆 PERFORMANCE SUMMARY")
        print("=" * 60)
        
        if best:
            best_pct = self.calculate_stock_percentage(best)
            print(f"Best Performer:  {best['symbol']} ({best_pct:+.2f}%)")
        
        if worst:
            worst_pct = self.calculate_stock_percentage(worst)
            print(f"Worst Performer: {worst['symbol']} ({worst_pct:+.2f}%)")
        
        print("=" * 60)


def main():
    """Main program to run the stock portfolio tracker."""
    portfolio = StockPortfolio()
    
    while True:
        print("\n" + "=" * 60)
        print("STOCK PORTFOLIO TRACKER")
        print("=" * 60)
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Update Stock Price")
        print("4. View Portfolio")
        print("5. Performance Summary")
        print("6. Exit")
        print("=" * 60)
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ")
            try:
                quantity = int(input("Enter quantity: "))
                purchase_price = float(input("Enter purchase price per share: ₹"))
                portfolio.add_stock(symbol, quantity, purchase_price)
            except ValueError:
                print("✗ Invalid input. Please enter valid numbers.")
        
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ")
            portfolio.remove_stock(symbol)
        
        elif choice == '3':
            symbol = input("Enter stock symbol: ")
            try:
                new_price = float(input("Enter new price: ₹"))
                portfolio.update_price(symbol, new_price)
            except ValueError:
                print("✗ Invalid price. Please enter a valid number.")
        
        elif choice == '4':
            portfolio.display_portfolio()
        
        elif choice == '5':
            portfolio.show_performance_summary()
        
        elif choice == '6':
            print("\n👋 Thank you for using Stock Portfolio Tracker!")
            break
        
        else:
            print("✗ Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()